#!/bin/bash

APPS="
astrobin
rawdata
nested_comments
astrobin_apps_users
astrobin_apps_images
astrobin_apps_platesolving
astrobin_apps_donations
astrobin_apps_premium
astrobin_apps_groups
astrobin_apps_notifications
astrobin_apps_iotd
astrobin_apps_landing
"

for APP in ${APPS}; do
    echo "Processing ${APP}..."
    (cd ${APP}; ../manage.py compilemessages)
done
