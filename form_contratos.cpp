#include "form_contratos.h"
#include "ui_form_contratos.h"

form_Contratos::form_Contratos(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_Contratos)
{
    ui->setupUi(this);
}

form_Contratos::~form_Contratos()
{
    delete ui;
}
