#include "form_actualizarprofesionales.h"
#include "ui_form_actualizarprofesionales.h"

form_actualizarprofesionales::form_actualizarprofesionales(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_actualizarprofesionales)
{
    ui->setupUi(this);
}

form_actualizarprofesionales::~form_actualizarprofesionales()
{
    delete ui;
}
