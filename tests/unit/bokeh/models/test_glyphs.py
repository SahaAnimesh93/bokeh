# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2019, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Boilerplate
# -----------------------------------------------------------------------------
import pytest  # noqa isort:skip

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Bokeh imports
from _util_models import (
    FILL,
    GLYPH,
    HATCH,
    LINE,
    MARKER,
    TEXT,
    check_fill_properties,
    check_hatch_properties,
    check_line_properties,
    check_marker_properties,
    check_properties_existence,
    check_text_properties,
)
from bokeh.core.enums import (
    Anchor,
    AngleUnits,
    ButtonType,
    DashPattern,
    Dimension,
    Direction,
    FontStyle,
    LegendLocation,
    LineCap,
    LineDash,
    LineJoin,
    Location,
    MapType,
)
from bokeh.core.enums import NamedColor as Color
from bokeh.core.enums import TextAlign, TextBaseline
from bokeh.models.glyphs import (
    Asterisk,
    CircleCross,
    CircleX,
    Cross,
    Dash,
    Diamond,
    DiamondCross,
    InvertedTriangle,
    Square,
    SquareCross,
    SquareX,
    Triangle,
    X,
)

# Module under test
from bokeh.models.glyphs import (  # isort:skip
    AnnularWedge,
    Annulus,
    Arc,
    Bezier,
    Circle,
    HArea,
    HBar,
    Image,
    ImageRGBA,
    ImageURL,
    Line,
    MultiLine,
    MultiPolygons,
    Oval,
    Patch,
    Patches,
    Quad,
    Quadratic,
    Ray,
    Rect,
    Segment,
    Step,
    Text,
    VArea,
    VBar,
    Wedge,
)


# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------


# fool flake8
(
    LineJoin,
    LineDash,
    LineCap,
    FontStyle,
    TextAlign,
    TextBaseline,
    Direction,
    AngleUnits,
    Dimension,
    Anchor,
    Location,
    LegendLocation,
    DashPattern,
    ButtonType,
    MapType,
    Color,
)

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------


def test_AnnularWedge():
    glyph = AnnularWedge()
    assert glyph.x is None
    assert glyph.y is None
    assert glyph.inner_radius is None
    assert glyph.outer_radius is None
    assert glyph.start_angle is None
    assert glyph.end_angle is None
    assert glyph.direction == "anticlock"
    check_fill_properties(glyph)
    check_line_properties(glyph)
    check_properties_existence(
        glyph,
        [
            "x",
            "y",
            "inner_radius",
            "inner_radius_units",
            "outer_radius",
            "outer_radius_units",
            "start_angle",
            "start_angle_units",
            "end_angle",
            "end_angle_units",
            "direction",
        ],
        FILL,
        LINE,
        GLYPH,
    )


def test_Annulus():
    glyph = Annulus()
    assert glyph.x is None
    assert glyph.y is None
    assert glyph.inner_radius is None
    assert glyph.outer_radius is None
    check_fill_properties(glyph)
    check_line_properties(glyph)
    check_properties_existence(
        glyph,
        ["x", "y", "inner_radius", "inner_radius_units", "outer_radius", "outer_radius_units"],
        FILL,
        LINE,
        GLYPH,
    )


def test_Arc():
    glyph = Arc()
    assert glyph.x is None
    assert glyph.y is None
    assert glyph.radius is None
    assert glyph.start_angle is None
    assert glyph.end_angle is None
    assert glyph.direction == "anticlock"
    check_line_properties(glyph)
    check_properties_existence(
        glyph,
        [
            "x",
            "y",
            "radius",
            "radius_units",
            "start_angle",
            "start_angle_units",
            "end_angle",
            "end_angle_units",
            "direction",
        ],
        LINE,
        GLYPH,
    )


def test_Bezier():
    glyph = Bezier()
    assert glyph.x0 is None
    assert glyph.y0 is None
    assert glyph.x1 is None
    assert glyph.y1 is None
    assert glyph.cx0 is None
    assert glyph.cy0 is None
    assert glyph.cx1 is None
    assert glyph.cy1 is None
    check_line_properties(glyph)
    check_properties_existence(
        glyph, ["x0", "y0", "x1", "y1", "cx0", "cy0", "cx1", "cy1"], LINE, GLYPH
    )


def test_HArea():
    glyph = HArea()
    assert glyph.y is None
    assert glyph.x1 is None
    assert glyph.x2 is None
    check_fill_properties(glyph)
    check_hatch_properties(glyph)
    check_properties_existence(glyph, ["y", "x1", "x2"], FILL, HATCH, GLYPH)


def test_HBar():
    glyph = HBar()
    assert glyph.y is None
    assert glyph.height is None
    assert glyph.left == 0
    assert glyph.right is None
    check_fill_properties(glyph)
    check_hatch_properties(glyph)
    check_line_properties(glyph)
    check_properties_existence(glyph, ["y", "height", "left", "right"], FILL, HATCH, LINE, GLYPH)


def test_Image():
    glyph = Image()
    assert glyph.image is None
    assert glyph.x is None
    assert glyph.y is None
    assert glyph.dw is None
    assert glyph.dh is None
    assert glyph.dilate is False
    check_properties_existence(
        glyph,
        [
            "image",
            "x",
            "y",
            "dw",
            "dw_units",
            "dh",
            "dh_units",
            "global_alpha",
            "dilate",
            "color_mapper",
        ],
        GLYPH,
    )


def test_ImageRGBA():
    glyph = ImageRGBA()
    assert glyph.image is None
    assert glyph.x is None
    assert glyph.y is None
    assert glyph.dw is None
    assert glyph.dh is None
    assert glyph.dilate is False
    check_properties_existence(
        glyph,
        ["image", "x", "y", "dw", "dw_units", "dh", "dh_units", "global_alpha", "dilate"],
        GLYPH,
    )


def test_ImageURL():
    glyph = ImageURL()
    assert glyph.url is None
    assert glyph.x is None
    assert glyph.y is None
    assert glyph.w is None
    assert glyph.h is None
    assert glyph.angle == 0
    assert glyph.dilate is False
    assert glyph.anchor == Anchor.top_left
    assert glyph.retry_attempts == 0
    assert glyph.retry_timeout == 0
    assert glyph.global_alpha == 1.0
    check_properties_existence(
        glyph,
        [
            "url",
            "x",
            "y",
            "w",
            "w_units",
            "h",
            "h_units",
            "angle",
            "angle_units",
            "dilate",
            "anchor",
            "retry_attempts",
            "retry_timeout",
            "global_alpha",
        ],
        GLYPH,
    )


def test_Line():
    glyph = Line()
    assert glyph.x is None
    assert glyph.y is None
    check_line_properties(glyph)
    check_properties_existence(glyph, ["x", "y"], LINE, GLYPH)


def test_MultiLine():
    glyph = MultiLine()
    assert glyph.xs is None
    assert glyph.ys is None
    check_line_properties(glyph)
    check_properties_existence(glyph, ["xs", "ys"], LINE, GLYPH)


def test_MultiPolygons():
    glyph = MultiPolygons()
    assert glyph.xs is None
    assert glyph.ys is None
    check_fill_properties(glyph)
    check_hatch_properties(glyph)
    check_line_properties(glyph)
    check_properties_existence(glyph, ["xs", "ys"], FILL, HATCH, LINE, GLYPH)


def test_Oval():
    glyph = Oval()
    assert glyph.x is None
    assert glyph.y is None
    assert glyph.width is None
    assert glyph.height is None
    assert glyph.angle == 0
    check_fill_properties(glyph)
    check_line_properties(glyph)
    check_properties_existence(
        glyph,
        ["x", "y", "width", "width_units", "height", "height_units", "angle", "angle_units"],
        FILL,
        LINE,
        GLYPH,
    )


def test_Patch():
    glyph = Patch()
    assert glyph.x is None
    assert glyph.y is None
    check_fill_properties(glyph)
    check_hatch_properties(glyph)
    check_line_properties(glyph)
    check_properties_existence(glyph, ["x", "y"], FILL, HATCH, LINE, GLYPH)


def test_Patches():
    glyph = Patches()
    assert glyph.xs is None
    assert glyph.ys is None
    check_fill_properties(glyph)
    check_hatch_properties(glyph)
    check_line_properties(glyph)
    check_properties_existence(glyph, ["xs", "ys"], FILL, HATCH, LINE, GLYPH)


def test_Quad():
    glyph = Quad()
    assert glyph.left is None
    assert glyph.right is None
    assert glyph.bottom is None
    assert glyph.top is None
    check_fill_properties(glyph)
    check_hatch_properties(glyph)
    check_line_properties(glyph)
    check_properties_existence(glyph, ["left", "right", "bottom", "top"], FILL, HATCH, LINE, GLYPH)


def test_Quadratic():
    glyph = Quadratic()
    assert glyph.x0 is None
    assert glyph.y0 is None
    assert glyph.x1 is None
    assert glyph.y1 is None
    assert glyph.cx is None
    assert glyph.cy is None
    check_line_properties(glyph)
    check_properties_existence(glyph, ["x0", "y0", "x1", "y1", "cx", "cy"], LINE, GLYPH)


def test_Ray():
    glyph = Ray()
    assert glyph.x is None
    assert glyph.y is None
    assert glyph.angle is None
    assert glyph.length is None
    check_line_properties(glyph)
    check_properties_existence(
        glyph, ["x", "y", "angle", "angle_units", "length", "length_units"], LINE, GLYPH
    )


def test_Rect():
    glyph = Rect()
    assert glyph.x is None
    assert glyph.y is None
    assert glyph.width is None
    assert glyph.height is None
    assert glyph.angle == 0
    assert glyph.dilate is False
    check_fill_properties(glyph)
    check_line_properties(glyph)
    check_properties_existence(
        glyph,
        [
            "x",
            "y",
            "width",
            "width_units",
            "height",
            "height_units",
            "angle",
            "angle_units",
            "dilate",
        ],
        FILL,
        LINE,
        GLYPH,
    )


def test_Segment():
    glyph = Segment()
    assert glyph.x0 is None
    assert glyph.y0 is None
    assert glyph.x1 is None
    assert glyph.y1 is None
    check_line_properties(glyph)
    check_properties_existence(glyph, ["x0", "y0", "x1", "y1"], LINE, GLYPH)


def test_Step():
    glyph = Step()
    assert glyph.x is None
    assert glyph.y is None
    assert glyph.mode == "before"
    check_line_properties(glyph)
    check_properties_existence(glyph, ["x", "y", "mode"], LINE, GLYPH)


def test_Text():
    glyph = Text()
    assert glyph.x is None
    assert glyph.y is None
    assert glyph.text == "text"
    assert glyph.angle == 0
    check_text_properties(glyph)
    check_properties_existence(
        glyph, ["x", "y", "text", "angle", "angle_units", "x_offset", "y_offset"], TEXT, GLYPH
    )


def test_VArea():
    glyph = VArea()
    assert glyph.x is None
    assert glyph.y1 is None
    assert glyph.y2 is None
    check_fill_properties(glyph)
    check_hatch_properties(glyph)
    check_properties_existence(glyph, ["x", "y1", "y2"], FILL, HATCH, GLYPH)


def test_VBar():
    glyph = VBar()
    assert glyph.x is None
    assert glyph.width is None
    assert glyph.top is None
    assert glyph.bottom == 0
    check_fill_properties(glyph)
    check_hatch_properties(glyph)
    check_line_properties(glyph)
    check_properties_existence(glyph, ["x", "width", "top", "bottom"], FILL, HATCH, LINE, GLYPH)


def test_Wedge():
    glyph = Wedge()
    assert glyph.x is None
    assert glyph.y is None
    assert glyph.radius is None
    assert glyph.start_angle is None
    assert glyph.end_angle is None
    assert glyph.direction == "anticlock"
    check_fill_properties(glyph)
    check_line_properties(glyph)
    check_properties_existence(
        glyph,
        [
            "x",
            "y",
            "radius",
            "radius_units",
            "start_angle",
            "start_angle_units",
            "end_angle",
            "end_angle_units",
            "direction",
        ],
        FILL,
        LINE,
        GLYPH,
    )


def test_Asterisk():
    marker = Asterisk()
    check_marker_properties(marker)
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(marker, MARKER, FILL, LINE, GLYPH)


def test_Circle():
    marker = Circle()
    check_marker_properties(marker)
    assert marker.radius is None
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(
        marker, ["radius", "radius_units", "radius_dimension"], MARKER, FILL, LINE, GLYPH
    )


def test_CircleCross():
    marker = CircleCross()
    check_marker_properties(marker)
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(marker, MARKER, FILL, LINE, GLYPH)


def test_CircleX():
    marker = CircleX()
    check_marker_properties(marker)
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(marker, MARKER, FILL, LINE, GLYPH)


def test_Cross():
    marker = Cross()
    check_marker_properties(marker)
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(marker, MARKER, FILL, LINE, GLYPH)


def test_Dash():
    marker = Dash()
    check_marker_properties(marker)
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(marker, MARKER, FILL, LINE, GLYPH)


def test_Diamond():
    marker = Diamond()
    check_marker_properties(marker)
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(marker, MARKER, FILL, LINE, GLYPH)


def test_DiamondCross():
    marker = DiamondCross()
    check_marker_properties(marker)
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(marker, MARKER, FILL, LINE, GLYPH)


def test_InvertedTriangle():
    marker = InvertedTriangle()
    check_marker_properties(marker)
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(marker, MARKER, FILL, LINE, GLYPH)


def test_Square():
    marker = Square()
    check_marker_properties(marker)
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(marker, MARKER, FILL, LINE, GLYPH)


def test_SquareCross():
    marker = SquareCross()
    check_marker_properties(marker)
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(marker, MARKER, FILL, LINE, GLYPH)


def test_SquareX():
    marker = SquareX()
    check_marker_properties(marker)
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(marker, MARKER, FILL, LINE, GLYPH)


def test_Triangle():
    marker = Triangle()
    check_marker_properties(marker)
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(marker, MARKER, FILL, LINE, GLYPH)


def test_X():
    marker = X()
    check_marker_properties(marker)
    check_fill_properties(marker)
    check_line_properties(marker)
    check_properties_existence(marker, MARKER, FILL, LINE, GLYPH)


# -----------------------------------------------------------------------------
# Dev API
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Private API
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Code
# -----------------------------------------------------------------------------
