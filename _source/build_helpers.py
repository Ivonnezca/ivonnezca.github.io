import math

def chirp_path(w=560, h=46, n=420):
    """A gravitational-wave chirp: frequency and amplitude grow, then ring down."""
    pts = []
    tc = 0.86
    for k in range(n + 1):
        x = k / n
        if x < tc:
            tau = tc - x + 0.012
            amp = 0.10 + 0.9 * (0.012 / tau) ** 0.25
            phase = -2 * math.pi * 16 * (tau / tc) ** 0.625
        else:
            amp = math.exp(-(x - tc) * 38)
            phase = 2 * math.pi * 26 * (x - tc)
        y = h / 2 - amp * (h / 2 - 2) * math.sin(phase)
        pts.append(f"{x * w:.1f},{y:.1f}")
    return "M" + " L".join(pts)


