from django.http import HttpResponse


def check_N(N, alpha):
    if N not in range(0, len(alpha) + 1):
        return HttpResponse(status=400)
    else:
        return N
