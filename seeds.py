from app import db
from app.models.tables import Atividade
from datetime import date

a1= Atividade(nome='Oficina de Git Hub', tipo='Oficina', data=date(2019, 10, 2), carga_horario=8, arquivo='/1/348384.pdf', usuario_id=1)

a2= Atividade(nome='BigData', tipo='Palestra', data=date(2020, 3, 12), carga_horario=1, arquivo='/1/352145.pdf', usuario_id=1)

a3= Atividade(nome='Oficina Jekyll', tipo='Oficina', data=date(2020, 12, 13), carga_horario=10, arquivo='/1/457895.pdf', usuario_id=1)

db.session.add(a1)
db.session.add(a2)
db.session.add(a3)

db.session.commit()
