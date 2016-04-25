SFM Docker
----------

Provides docker-compose.yml files for deploying [Social Feed Manager](https://gwu-libraries.github.io/sfm-ui).

For instructions for deploying SFM using Docker, see [the docs](http://sfm.readthedocs.org/en/latest/install.html).

Smoke tests
===========

1. Start an SFM instance using Docker.

        docker-compose -f master.docker-compose.yml up -d

2. Pull the smoke test container.

        docker pull gwul/sfm-docker-smoke
        
3. Run the tests.

        docker run --rm --link sfmdocker_sfmmasterrabbit_1:mq --link sfmdocker_sfmmasterapp_1:ui gwul/sfm-docker-smoke

Notes:

* The container names should be consistent (e.g., `sfmdocker_sfmmasterrabbit_1`).  However, if they're not get the
   correct names using `docker ps`.
* While developing new tests, share a volume that contains the code.  For example, add 
   `--volume ~/sfm-docker:/opt/sfm-test` to `docker run`.
 
*Each new component should add at least one test to verify that it is up and running.*
