from .colors import BackgroundColors


class DoorMat():
    def top(width):
        BackgroundColors.printColor(
            value=" Check if TODO or FIXME exist ".center(width, "*"),
            color=BackgroundColors.CYAN
        )

    def middle(width):
        BackgroundColors.printColor(
            value=" End Check & Continu ".center(width, "*"),
            color=BackgroundColors.CYAN
        )

    def bottom(width):
        BackgroundColors.printColor(
            value=" Issues created ".center(width, "*"),
            color=BackgroundColors.CYAN
        )
