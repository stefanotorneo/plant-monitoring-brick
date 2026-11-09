"""Plant Monitoring brick: checks light levels for plant care."""

__version__ = "1.1.0"

LIGHT_THRESHOLD = 300


def is_light_sufficient(light_level: float, threshold: float = LIGHT_THRESHOLD) -> bool:
    """Return True if the light level is at or above the threshold."""
    return light_level >= threshold


def describe_light(light_level: float) -> str:
    """Return a short human-readable description of the light level."""
    if light_level < 100:
        return "dark"
    if light_level < LIGHT_THRESHOLD:
        return "dim"
    return "bright"
