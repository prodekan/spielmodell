initDB <- function()
{
  database <- "spielmodell";
  con <- dbConnect(MySQL(), user="root", password="selver365", host="localhost",
                   db=database, client.flag=CLIENT_MULTI_RESULTS);
  
}