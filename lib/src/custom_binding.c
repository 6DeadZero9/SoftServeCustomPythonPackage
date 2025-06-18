#include <stddef.h>

#include <openssl/rsa.h>
#include <openssl/bn.h>
#include <openssl/pem.h>
#include <openssl/bio.h>

#include <custom_binding.h>

int generate_key(int bits, char *buffer, int buffer_size)
{
    int ret = 0;
    EVP_PKEY *key = EVP_RSA_gen(bits);
    BIO *bio = BIO_new(BIO_s_mem());
    EVP_PKEY_print_public(bio, key, 4, NULL);

    ret = BIO_read(bio, buffer, buffer_size);

    BIO_free_all(bio);
    EVP_PKEY_free(key);

    return (ret == 1);
}