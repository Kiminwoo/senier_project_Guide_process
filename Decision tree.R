install.packages("rpart")

library(rpart)


c <- rpart(Species ~., data = iris)

c



plot(c, compress = T, margin=0.3)

text(c, cex=1.5)

head(predict(c, newdata=iris, type="class"))

tail(predict(c, newdata=iris, type="class"))

#--------------------------------------rpart.plot

install.packages("rpart.plot")

library(rpart.plot)

prp(c, type=4, extra=2)

ls(c)

c$cptable

opt <- which.min(c$cptable[,"xerror"])

cp <- c$cptable[opt,"CP"]

prune.c <- prune(c, cp = cp)

plot(prune.c)

text(prune.c, use.n = T)

plotcp(c)

#-------------------------------------party

install.packages("party")

library(party)

data("stagec")

str(stagec)

stagec1 <- subset(stagec, !is.na(g2))
stagec2 <- subset(stagec1, !is.na(gleason))
stagec3 <- subset(stagec2, !is.na(eet))

str(stagec3)

set.seed(1234)

ind <- sample(2, nrow(stagec3), replace=TRUE, prob = c(0.7,0.3))

trainData <- stagec3[ind==1,]
testData <- stagec3[ind==2,]

tree <- ctree(ploidy ~., data=trainData)

tree

plot(tree)


testPred = predict(tree, newdata=testData)

table(testPred, testData$ploidy)


#------------------------------- airquality

airq <- subset(airquality, !is.na(Ozone))

head(airq)

airct <- ctree(Ozone ~ ., data=airq)

airct

plot(airct)

head(predict(airct, data=airq))

predict(airct, data=airq)

predict(airct, data=airq, type="node")

mean((airq$Ozone - predict(airct))^2)