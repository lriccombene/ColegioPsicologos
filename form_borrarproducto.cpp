#include "form_borrarproducto.h"
#include "ui_form_borrarproducto.h"

form_borrarproducto::form_borrarproducto(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_borrarproducto)
{
    ui->setupUi(this);
}

form_borrarproducto::~form_borrarproducto()
{
    delete ui;
}
