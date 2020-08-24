from django.shortcuts import render


def test_view(request):
    return render(request, 'business/campaign_create.html', {})


def campaign_list(request):
    return render(request, 'business/campaign_list.html', {})


def profile_create(request):
    return render(request, 'user/profile_create.html', {})


def influencers_assignment(request):
    return render(request, 'influencer/assignment_list.html', {})


def campaign_detail(request):
    return render(request, 'business/campaign_detail.html', {})


def memer_assignment(request):
    return render(request, 'memer/list.html', {})
