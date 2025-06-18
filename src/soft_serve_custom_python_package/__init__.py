from pathlib import Path
import ctypes


def rsa_c_passthrough(rsa_bits=4096):
    lib_path = Path(__file__).parent / "libSoftServeExampleCBinding.so"

    if not lib_path.exists():
        raise FileNotFoundError(f"Shared library not found: {lib_path}")

    loaded_lib = ctypes.CDLL(lib_path)
    loaded_lib.generate_key.argtypes = [
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_char),
        ctypes.c_int,
    ]
    loaded_lib.generate_key.restype = ctypes.c_int

    buffer_size = rsa_bits // 8
    buffer = ctypes.create_string_buffer(buffer_size)
    res = loaded_lib.generate_key(rsa_bits, buffer, buffer_size)

    return buffer.raw.decode()
