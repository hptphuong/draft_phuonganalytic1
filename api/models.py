from __future__ import unicode_literals
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table

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

class user_daily(Model):
    m_date = columns.DateTime(primary_key=True)
    userid = columns.Text(primary_key=True)
    fsa = columns.Text(required=True,primary_key=True)
    fsid = columns.Text(required=False,primary_key=True)
    ck_new = columns.Integer()
    class Meta:
        get_pk_field='fsa'

class user_daily_report(Model):
	bucket=columns.Integer(primary_key=True)
	m_date= columns.Date(primary_key=True,clustering_order="DESC")
	users=columns.Integer()

	
# class Comment(Model):
#     # photo_id = columns.UUID(primary_key=True)
#     comment_id = columns.TimeUUID(primary_key=True)
#     comment = columns.Text()
