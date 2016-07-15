#include "form_serviciodecontratos.h"
#include "ui_form_serviciodecontratos.h"

form_serviciodecontratos::form_serviciodecontratos(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_serviciodecontratos)
{
    ui->setupUi(this);
}

form_serviciodecontratos::~form_serviciodecontratos()
{
    delete ui;
}
