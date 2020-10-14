-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`First_Name`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`First_Name` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `FIRST` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Last_Name`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Last_Name` (
  `ID` INT NOT NULL,
  `LAST` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE)
ENGINE = InnoDB
COMMENT = 'FIRST_NAME';


-- -----------------------------------------------------
-- Table `mydb`.`First Name_has_Last Name`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`First Name_has_Last Name` (
  `First Name_ID` INT NOT NULL,
  `Last Name_ID` INT NOT NULL,
  PRIMARY KEY (`First Name_ID`, `Last Name_ID`),
  INDEX `fk_First Name_has_Last Name_Last Name1_idx` (`Last Name_ID` ASC) VISIBLE,
  INDEX `fk_First Name_has_Last Name_First Name_idx` (`First Name_ID` ASC) VISIBLE,
  CONSTRAINT `fk_First Name_has_Last Name_First Name`
    FOREIGN KEY (`First Name_ID`)
    REFERENCES `mydb`.`First_Name` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_First Name_has_Last Name_Last Name1`
    FOREIGN KEY (`Last Name_ID`)
    REFERENCES `mydb`.`Last_Name` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`First_Name_has_Last_Name`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`First_Name_has_Last_Name` (
  `First_Name_ID` INT NOT NULL,
  `Last_Name_ID` INT NOT NULL,
  PRIMARY KEY (`First_Name_ID`, `Last_Name_ID`),
  INDEX `fk_First_Name_has_Last_Name_Last_Name1_idx` (`Last_Name_ID` ASC) VISIBLE,
  INDEX `fk_First_Name_has_Last_Name_First_Name1_idx` (`First_Name_ID` ASC) VISIBLE,
  CONSTRAINT `fk_First_Name_has_Last_Name_First_Name1`
    FOREIGN KEY (`First_Name_ID`)
    REFERENCES `mydb`.`First_Name` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_First_Name_has_Last_Name_Last_Name1`
    FOREIGN KEY (`Last_Name_ID`)
    REFERENCES `mydb`.`Last_Name` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
