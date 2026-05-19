THEMES = {
    "publication": {
        "facecolor": "white",
        "axis": "off",
        "title_size": 16,
        "subtitle_size": 11,
        "source_size": 8,
    },
    "minimal": {
        "facecolor": "white",
        "axis": "off",
        "title_size": 14,
        "subtitle_size": 10,
        "source_size": 8,
    },
    "dark": {
        "facecolor": "#111111",
        "axis": "off",
        "title_size": 16,
        "subtitle_size": 11,
        "source_size": 8,
    },
}


def list_themes() -> list[str]:
    return sorted(THEMES)


def apply_theme(fig, ax, theme: str, title=None, subtitle=None, source_note=None) -> None:
    settings = THEMES.get(theme, THEMES["publication"])
    fig.patch.set_facecolor(settings["facecolor"])
    ax.set_facecolor(settings["facecolor"])
    if settings["axis"] == "off":
        ax.set_axis_off()

    if title:
        ax.set_title(title, fontsize=settings["title_size"], loc="left", pad=12)
    if subtitle:
        ax.text(
            0,
            1.01,
            subtitle,
            transform=ax.transAxes,
            fontsize=settings["subtitle_size"],
            ha="left",
        )
    if source_note:
        ax.text(
            0,
            -0.04,
            source_note,
            transform=ax.transAxes,
            fontsize=settings["source_size"],
            ha="left",
            va="top",
        )
