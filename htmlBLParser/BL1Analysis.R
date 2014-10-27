library(RMySQL)

initDB <- function()
{
  ldatabase <- "spielmodell";
  luser <- "root";
  lpass <- "selver365";
  lhost <- "localhost";
  paste("initDB with ", luser, lpass, lhost, ldatabase, sep = " ")
  
  con <- dbConnect(MySQL(), user=luser, password=lpass, host=lhost,
                   db=ldatabase, client.flag=CLIENT_MULTI_RESULTS);
  
}



clearDB <- function(conn) 
{
  print("clearDB");
  dbDisconnect(conn);
}