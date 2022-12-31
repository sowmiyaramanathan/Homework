CREATE TABLE `users_data`.`tbl_users` (
  `userID` INT NOT NULL AUTO_INCREMENT,
  `userName` VARCHAR(45) NOT NULL,
  `userEmail` VARCHAR(45) NOT NULL,
  `userPassword` VARCHAR(45) NOT NULL,
  `userPhoneNumber` VARCHAR(45) NOT NULL,
  `userRollNumber` VARCHAR(45) NOT NULL,
  `userRegNumber` VARCHAR(45) NOT NULL,
  `userYearOfStudy` VARCHAR(45) NOT NULL,
  `userInDept` VARCHAR(45) NOT NULL,
  `userInSection` VARCHAR(45) NOT NULL,
  `userJoinedOn` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`userID`),
  UNIQUE INDEX `userID_UNIQUE` (`userID` ASC) VISIBLE);
