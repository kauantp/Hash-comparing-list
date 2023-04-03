import hashlib

a = "Em 1999 iniciam-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação."
c = hashlib.sha256(a.encode())
b = hashlib.md5(a.encode())

cr ="c034489664dd98c3a2b0d7c1afc0717378827d9fa778288c8bb1c567c8bc2ec1"
br ="19406b49ace5073c806a79061f58dbd3"

cn = str(c.hexdigest())
bn = str(b.hexdigest())

if (cn == cr):
    print("Correto")
else:
    print("INCORRETO")
if (bn == br):
    print("Correto2")
else:
    print("INCORRETO2")

