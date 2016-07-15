#ifndef FORM_BUSCARPRODUCTO_H
#define FORM_BUSCARPRODUCTO_H

#include <QDialog>

namespace Ui {
class form_buscarproducto;
}

class form_buscarproducto : public QDialog
{
    Q_OBJECT

public:
    explicit form_buscarproducto(QWidget *parent = 0);
    ~form_buscarproducto();

private:
    Ui::form_buscarproducto *ui;
};

#endif // FORM_BUSCARPRODUCTO_H
