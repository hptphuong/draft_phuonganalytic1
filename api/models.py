from __future__ import unicode_literals
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

#User model
# CREATE TABLE test.fsa_site (
#     idsite text,
#     login text,
#     name text,
#     url text,)
class fsa_site(DjangoCassandraModel):
    idsite = columns.Text(primary_key=True)
    login = columns.Text(required=False)
    name = columns.Text(required=False)
    password = columns.Text(required=True)
    url = columns.Text(required=False)

class fsa_user(DjangoCassandraModel):
	# idsite = columns.Text(primary_key=True)
	# login = columns.Text(required=False)
	# name = columns.Text(required=False)
	# password = columns.Text(required=True)
	# url = columns.Text(required=False)
    login =columns.Text(primary_key=True)
    alias =columns.Text(required=False)
    date_registered=columns.Date()
    email =columns.Text(required=False)
    password =columns.Text(required=False)

class user_daily(DjangoCassandraModel):
	"""docstring for ClassName"""
	userid = columns.Text(primary_key=True)
	fsa = columns.Text(required=True,primary_key=True)
	fsid = columns.Text(required=False,primary_key=True)
	m_date =columns.DateTime()
	ck_new = columns.Integer()
	class Meta:
  		get_pk_field='fsa'
    


