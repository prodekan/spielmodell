library(XML)
connectToSite <- function()
{
  setwd('/home/selver/PycharmProjects/htmlBLParser/');
  htmlP <- htmlTreeParse(file = 'tipico_bl1.html', useInternalNodes = T);
  search <- '//div'
  title <- xpathApply(htmlP,  search, xmlValue);
  print(title)
}

