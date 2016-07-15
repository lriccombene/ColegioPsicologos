#include "form_buscarproducto.h"
#include "ui_form_buscarproducto.h"

form_buscarproducto::form_buscarproducto(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_buscarproducto)
{
    ui->setupUi(this);
}

form_buscarproducto::~form_buscarproducto()
{
    delete ui;
}
