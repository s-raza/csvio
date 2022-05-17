import os

import pytest
from python_on_whales import docker

from csvio.csvreader import CSVReader
from csvio.remote import FTPReader


@pytest.fixture(scope="module")
def docker_ftp_details(request):

    os.chdir(request.fspath.dirname)
    print(": Starting FTP server in docker... ", end="", flush=True)
    docker.compose.up(detach=True)
    print("Started... Running tests... ", end="", flush=True)

    docker_config = docker.compose.config()
    ftp_config = docker_config.services["ftp"]
    docker_volume = ftp_config.volumes[0]
    remote_dir = docker_volume.target.split("/")[-1]

    docker_env = ftp_config.environment

    ftp_details = {
        "hostname": docker_env["PASV_ADDRESS"],
        "username": docker_env["FTP_USER"],
        "password": docker_env["FTP_PASS"],
        "remote_dir": remote_dir,
        "remote_file": "sample_products.csv",
    }

    # Function for teardown operations
    def fin():

        print(" Tests done... Stopping FTP Server... ", end="", flush=True)
        docker.compose.down()

        print("Stopped")
        os.chdir(request.config.invocation_dir)

    request.addfinalizer(fin)

    return ftp_details


def test_ftp_reader(docker_ftp_details):

    ftpreader = FTPReader(docker_ftp_details, timeout=2, increment_timeout=1)

    csvreader = CSVReader("./sample_data/sample_products.csv")

    assert ftpreader.rows == csvreader.rows
