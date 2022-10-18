from typing import Union, Tuple, List, Optional, Dict, Sequence

from pygame.surface import Surface
from pygame.constants import FULLSCREEN
from ._common import _Coordinate, _RectValue, _ColorValue, _RgbaOutput

class _VidInfo:
    hw: int
    wm: int
    video_mem: int
    bitsize: int
    bytesize: int
    masks: _RgbaOutput
    shifts: _RgbaOutput
    losses: _RgbaOutput
    blit_hw: int
    blit_hw_CC: int
    blit_hw_A: int
    blit_sw: int
    blit_sw_CC: int
    blit_sw_A: int
    current_h: int
    current_w: int

def init() -> None: ...
def quit() -> None: ...
def get_init() -> bool: ...
def set_mode(
    size: _Coordinate = (0, 0),
    flags: int = 0,
    depth: int = 0,
    display: int = 0,
    vsync: int = 0,
) -> Surface: ...
def get_surface() -> Surface: ...
def flip() -> None: ...
def update(rectangle: Optional[Union[_RectValue, List[_RectValue]]] = None) -> None: ...
def get_driver() -> str: ...
def Info() -> _VidInfo: ...
def get_wm_info() -> Dict[str, int]: ...
def list_modes(
    depth: int = 0,
    flags: int = FULLSCREEN,
    display: int = 0,
) -> List[Tuple[int, int]]: ...
def mode_ok(
    size: Union[Sequence[int], Tuple[int, int]],
    flags: int = 0,
    depth: int = 0,
    display: int = 0,
) -> int: ...
def gl_get_attribute(flag: int) -> int: ...
def gl_set_attribute(flag: int, value: int) -> None: ...
def get_active() -> bool: ...
def iconify() -> bool: ...
def toggle_fullscreen() -> int: ...
def set_gamma(red: float, green: float = ..., blue: float = ...) -> int: ...
def set_gamma_ramp(
    red: Sequence[int], green: Sequence[int], blue: Sequence[int]
) -> int: ...
def set_icon(surface: Surface) -> None: ...
def set_caption(title: str, icontitle: Optional[str] = None) -> None: ...
def get_caption() -> Tuple[str, str]: ...
def set_palette(palette: Sequence[_ColorValue]) -> None: ...
def get_num_displays() -> int: ...
def get_window_size() -> Tuple[int, int]: ...
def get_allow_screensaver() -> bool: ...
def set_allow_screensaver(value: bool = True) -> None: ...
