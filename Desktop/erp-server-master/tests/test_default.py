from setupfixture import client, valid_admin_credentials, valid_hod_credentials
import pytest

def test_default_route(client):
    ''' tests Default route for server '''

    res = client.get("/",headers={'Authorization': 'Basic ' + valid_admin_credentials })
    assert res.status_code == 200
    assert b'LOL' == res.data

def test_default_hod(client):
    ''' tests Default route for server '''
    res = client.get("/",headers={'Authorization': 'Basic ' + valid_hod_credentials })
    assert res.status_code == 200
    assert b'LOL' == res.data