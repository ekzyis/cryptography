#!/usr/bin/env python

"""ChaCha20/r implementation.

Specification:
    https://cr.yp.to/chacha/chacha-20080128.pdf

Test vectors:
    https://tools.ietf.org/html/rfc7539 (IETF implementation; uses 96-bit nonce and 32-bit counter)
    https://tools.ietf.org/html/draft-strombergson-chacha-test-vectors-00 (original implementation)

Description of ChaCha20 from the specification paper used as a reference for this implementation:

    "ChaCha8 is a 256-bit stream cipher based on the 8-round cipher Salsa20/8.
    The changes from Salsa20/8 to ChaCha8 are designed to improve diffusion per round, conjecturally increasing
    resistance to cryptanalysis, while preserving—and often improving—time per round. ChaCha12 and ChaCha20 are
    analogous modifications of the 12-round and 20-round ciphers Salsa20/12 and Salsa20/20."
    - Daniel J. Bernstein, https://cr.yp.to/chacha/chacha-20080120.pdf
"""
from typing import Any

from bitstring import Bits

from util.bitseq import bitseq_split, bitseq_add
from util.rot import rot_left_bits

__CHACHA_20_ROUNDS__ = 20
__CHACHA_20_INITIAL_COUNTER__ = 0


def quarterround(y: Bits) -> Bits:
    """Calculate the ChaCha20 quarterround value of the input as specified in the paper.

    Returns a 128-bit value.
    Raises error if input is not 128-bit.
    """
    if len(y) != 128:
        raise ValueError("Input must be 64-bit")

    def _quarterround_step(x1, x2, x3, shift):
        x1 = bitseq_add(x1, x2)
        x3 ^= x1
        x3 = rot_left_bits(x3, shift)
        return x1, x2, x3

    a, b, c, d = bitseq_split(32, y)
    a, b, d = _quarterround_step(a, b, d, 16)
    c, d, b = _quarterround_step(c, d, b, 12)
    a, b, d = _quarterround_step(a, b, d, 8)
    c, d, b = _quarterround_step(c, d, b, 7)
    return a + b + c + d


def quarterround_state(state: Bits, i, j, k, l) -> Bits:
    """Calculate the quarterround value of the state with the given indices.

    Returns a 512-bit value.
    State must be 512-bit.
    """
    entry = bitseq_split(32, state)
    q = quarterround(sum([entry[i], entry[j], entry[k], entry[l]]))
    entry[i], entry[j], entry[k], entry[l] = bitseq_split(32, q)
    return sum(entry)


def chacha20_hash(state_: Bits) -> Bits:
    """Calculate the chacha20 hash value."""
    # copy old state
    state = Bits(state_)
    for i in range(int(__CHACHA_20_ROUNDS__ / 2)):
        # column round
        state = quarterround_state(state, 0, 4, 8, 12)
        state = quarterround_state(state, 1, 5, 9, 13)
        state = quarterround_state(state, 2, 6, 10, 14)
        state = quarterround_state(state, 3, 7, 11, 15)
        # diagonal round
        state = quarterround_state(state, 0, 5, 10, 15)
        state = quarterround_state(state, 1, 6, 11, 12)
        state = quarterround_state(state, 2, 7, 8, 13)
        state = quarterround_state(state, 3, 4, 9, 14)
    original_state_bitseq32 = bitseq_split(32, state_)
    new_state_bitseq32 = bitseq_split(32, state)
    state = sum([bitseq_add(xi, zi) for xi, zi in zip(original_state_bitseq32, new_state_bitseq32)])
    return state


def expansion(k: Bits, n: Bits) -> Bits:
    """Expand the key and the nonce into a 64-byte sequence.

    The hash function can be seen as working on following matrix where each entry is 32-bit (a 4-byte word).

          constant  constant  constant  constant
          key       key       key       key
          key       key       key       key
          counter   nonce     nonce     nonce

    The constants are part of the constant words sigma or tau.
    The input is the nonce (attacker-controlled input).

    Returns a 64-byte sequence.
    Raises error if key is not 256-bit or nonce is not 128-bit.
    """
    pass


def initial_counter() -> int:
    """Return the initial counter value."""
    return __CHACHA_20_INITIAL_COUNTER__


def xcrypt(k: Bits, text: Bits, *args: Any, **kwargs: Any) -> Bits:
    """En- or decrypt the message with the given key with ChaCha20.

    En- and decryption use the same algorithm because the inverse of XOR is XOR thus this function is called 'xcrypt'.

    En-/Decryption is done by XOR'ing the plain-/ciphertext with the stream generated by the expansion function.
    The nonce for the expansion function is dependent on current time thus ensuring that the same nonce
    will never be used again with the same key.

    The nonce for the expansion function should never be reused with the same key!
    Else, this happens: https://crypto.stackexchange.com/a/108/80458
    """
    pass


def encrypt(k: Bits, text: Bits) -> Bits:
    """Encrypt the message with the given key with ChaCha20.

    Make initialization vector dependent of current time to make sure a message is never
    encrypted again with the same key and IV.
    Raises error if key is not 256-bit.
    """
    pass
