from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import GameScore, Profile 
import json

# 🔒 Protect scanner page
@login_required
def home(request):
    return render(request, "games/home.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()   # regular user (no permissions)
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/register.html", {"form": form})


# 💾 Save AI result (AJAX)
@login_required   # optional but RECOMMENDED
def save_result(request):
    if request.method == "POST":
        data = json.loads(request.body)

        label = data.get("label")
        confidence = data.get("confidence")

        # For now just log it (later we save to DB)
        print("AI RESULT:", label, confidence)

        return JsonResponse({
            "status": "saved",
            "label": label,
            "confidence": confidence
        })

    return JsonResponse({"error": "Invalid request"}, status=400)

@login_required 
def games(request):
    return render(request, 'games/games.html')

# 🏆 Save Game Score (NEW)
@login_required
def save_score(request):
    if request.method == "POST":
        data = json.loads(request.body)

        game_name = data.get("game_name") or data.get("game")
        score = data.get("score")
        score_type = data.get("score_type", "LOW")

        if not game_name or score is None:
            return JsonResponse({"error": "Invalid data"}, status=400)

        # Save game score
        GameScore.objects.create(
            user=request.user,
            game_name=game_name,
            score=score,
            score_type=score_type
        )

        # Update global points
        profile, _ = Profile.objects.get_or_create(user=request.user)
        profile.points += 5
        profile.save()

        return JsonResponse({"status": "score_saved"})

    return JsonResponse({"error": "Invalid request"}, status=400)


# 📊 Leaderboard (OPTIONAL but READY)
@login_required
def leaderboard(request):
    game_name = request.GET.get("game", "Reaction Time")

    # Get score type for this game
    score_type = (
        GameScore.objects
        .filter(game_name=game_name)
        .values_list("score_type", flat=True)
        .first()
    ) or "LOW"

    # Ordering logic
    if score_type == "HIGH":
        scores = (
            GameScore.objects
            .filter(game_name=game_name)
            .order_by("-score", "created_at")[:10]
        )
    else:
        scores = (
            GameScore.objects
            .filter(game_name=game_name)
            .order_by("score", "created_at")[:10]
        )

    return render(request, "games/leaderboard.html", {
        "scores": scores,
        "game_name": game_name
    })
