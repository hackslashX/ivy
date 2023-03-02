# global
import math
from numbers import Number
from typing import Union, Optional, Tuple, List, Sequence, Iterable

import paddle

# local
import ivy
from ivy.utils.exceptions import IvyNotImplementedException

# noinspection PyProtectedMember
from ivy.functional.ivy.manipulation import _calculate_out_shape
from . import backend_version


# Array API Standard #
# -------------------#


def concat(
    xs: Union[Tuple[paddle.Tensor, ...], List[paddle.Tensor]],
    /,
    *,
    axis: Optional[int] = 0,
    out: Optional[paddle.Tensor] = None,
) -> paddle.Tensor:
    raise IvyNotImplementedException()


def expand_dims(
    x: paddle.Tensor,
    /,
    *,
    axis: Union[int, Sequence[int]] = 0,
    out: Optional[paddle.Tensor] = None,
) -> paddle.Tensor:
    return paddle.expand(x, axis)


def flip(
    x: paddle.Tensor,
    /,
    *,
    axis: Optional[Union[int, Sequence[int]]] = None,
    out: Optional[paddle.Tensor] = None,
) -> paddle.Tensor:
    raise IvyNotImplementedException()


def permute_dims(
    x: paddle.Tensor,
    /,
    axes: Tuple[int, ...],
    *,
    out: Optional[paddle.Tensor] = None,
) -> paddle.Tensor:
    return paddle.transpose(x, axes)


def _reshape_fortran_paddle(x, shape):
    if len(x.shape) > 0:
        x = paddle.transpose(x, list(reversed(range(len(x.shape)))))
    return paddle.transpose(paddle.reshape(x, shape[::-1]), list(range(len(shape)))[::-1])


def reshape(
    x: paddle.Tensor,
    /,
    shape: Union[ivy.NativeShape, Sequence[int]],
    *,
    copy: Optional[bool] = None,
    order: Optional[str] = "C",
    allowzero: Optional[bool] = True,
    out: Optional[paddle.Tensor] = None,
) -> paddle.Tensor:
    if not allowzero:
        shape = [
            new_s if con else old_s
            for new_s, con, old_s in zip(shape, paddle.to_tensor(shape) != 0, x.shape)
        ]
    if copy:
        newarr = paddle.clone(x)
        if order == "F":
            return _reshape_fortran_paddle(newarr, shape)
        return paddle.reshape(newarr, shape)
    if order == "F":
        return _reshape_fortran_paddle(x, shape)
    return paddle.reshape(x, shape)


def roll(
    x: paddle.Tensor,
    /,
    shift: Union[int, Sequence[int]],
    *,
    axis: Optional[Union[int, Sequence[int]]] = None,
    out: Optional[paddle.Tensor] = None,
) -> paddle.Tensor:
    raise IvyNotImplementedException()


def squeeze(
    x: paddle.Tensor,
    /,
    axis: Union[int, Sequence[int]],
    *,
    out: Optional[paddle.Tensor] = None,
) -> paddle.Tensor:
    raise IvyNotImplementedException()


def stack(
    arrays: Union[Tuple[paddle.Tensor], List[paddle.Tensor]],
    /,
    *,
    axis: int = 0,
    out: Optional[paddle.Tensor] = None,
) -> paddle.Tensor:
    raise IvyNotImplementedException()


# Extra #
# ------#


def split(
    x: paddle.Tensor,
    /,
    *,
    num_or_size_splits: Optional[Union[int, List[int]]] = None,
    axis: Optional[int] = 0,
    with_remainder: Optional[bool] = False,
) -> List[paddle.Tensor]:
    raise IvyNotImplementedException()


def repeat(
    x: paddle.Tensor,
    /,
    repeats: Union[int, Iterable[int]],
    *,
    axis: int = None,
    out: Optional[paddle.Tensor] = None,
) -> paddle.Tensor:
    raise IvyNotImplementedException()


def tile(
    x: paddle.Tensor, /, repeats: Sequence[int], *, out: Optional[paddle.Tensor] = None
) -> paddle.Tensor:
    if isinstance(repeats, paddle.Tensor):
        repeats = repeats.detach().cpu().numpy().tolist()
    return x.repeat(repeats)


def constant_pad(
    x: paddle.Tensor,
    /,
    pad_width: List[List[int]],
    *,
    value: Number = 0.0,
    out: Optional[paddle.Tensor] = None,
) -> paddle.Tensor:
    raise IvyNotImplementedException()


def zero_pad(
    x: paddle.Tensor,
    /,
    pad_width: List[List[int]],
    *,
    out: Optional[paddle.Tensor] = None,
):
    raise IvyNotImplementedException()


def swapaxes(
    x: paddle.Tensor, axis0: int, axis1: int, /, *, out: Optional[paddle.Tensor] = None
) -> paddle.Tensor:
    raise IvyNotImplementedException()


def clip(
    x: paddle.Tensor,
    x_min: Union[Number, paddle.Tensor],
    x_max: Union[Number, paddle.Tensor],
    /,
    *,
    out: Optional[paddle.Tensor] = None,
) -> paddle.Tensor:
    raise IvyNotImplementedException()


def unstack(
    x: paddle.Tensor, /, *, axis: int = 0, keepdims: bool = False
) -> List[paddle.Tensor]:
    raise IvyNotImplementedException()
