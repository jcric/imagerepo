$in =$args[0]

if ( $in -eq "backup")
{
    docker exec imagerepo-db-1 /usr/bin/mysqldump -u root --password=root links images > ./db/backup.sql
}

if ( $in -eq "restore")
{
    cat ./db/backup.sql | docker exec -i imagerepo-db-1 /usr/bin/mysql -u root --password=root links
}