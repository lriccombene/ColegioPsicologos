#include "form_actualizarproducto.h"
#include "ui_form_actualizarproducto.h"

form_actualizarproducto::form_actualizarproducto(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_actualizarproducto)
{
    ui->setupUi(this);
}

form_actualizarproducto::~form_actualizarproducto()
{
    delete ui;
}
