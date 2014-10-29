library(XML)
connectToSite <- function()
{
  setwd('/home/selver/PycharmProjects/htmlBLParser/');
  htmlP <- htmlTreeParse(file = 'tipico_bl1.html', useInternalNodes = T);
  title <- xpathApply(htmlP, "//title", xmlValue);

}

