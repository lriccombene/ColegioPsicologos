#include "form_borrarprofesionales.h"
#include "ui_form_borrarprofesionales.h"

form_borrarprofesionales::form_borrarprofesionales(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_borrarprofesionales)
{
    ui->setupUi(this);
}

form_borrarprofesionales::~form_borrarprofesionales()
{
    delete ui;
}
