from fastapi.PPA import PPA


PPA.exec("SELECT * FROM config where id!=1"),
# PPA.exec("SELECT * FROM config where id!={name}",{"name":1}),
# PPA.exec("SELECT * FROM config where id!=?",[1]),
# PPA.exec("SELECT * FROM config where id!=?", (1,)),