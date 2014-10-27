library(XML)
connectToSite <- function(url = "https://www.tipico.de/en/online-sports-betting/football/germany/bundesliga/g42301/")
{
  htmlP = htmlTreeParse(url, useInternalNodes = T);
  xpathSApply(htmlP, "//title", xmlValue)
}