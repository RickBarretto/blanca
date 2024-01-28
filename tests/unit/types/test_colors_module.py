from src.decoder import colors


def test_module_includes_all_colors():
    with open("tests/unit/types/colors", mode="r") as color_file:
        for color in color_file.readlines():
            assert color.strip() in colors.color_names