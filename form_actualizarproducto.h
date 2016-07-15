#ifndef FORM_ACTUALIZARPRODUCTO_H
#define FORM_ACTUALIZARPRODUCTO_H

#include <QDialog>

namespace Ui {
class form_actualizarproducto;
}

class form_actualizarproducto : public QDialog
{
    Q_OBJECT

public:
    explicit form_actualizarproducto(QWidget *parent = 0);
    ~form_actualizarproducto();

private:
    Ui::form_actualizarproducto *ui;
};

#endif // FORM_ACTUALIZARPRODUCTO_H
