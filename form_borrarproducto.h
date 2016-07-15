#ifndef FORM_BORRARPRODUCTO_H
#define FORM_BORRARPRODUCTO_H

#include <QDialog>

namespace Ui {
class form_borrarproducto;
}

class form_borrarproducto : public QDialog
{
    Q_OBJECT

public:
    explicit form_borrarproducto(QWidget *parent = 0);
    ~form_borrarproducto();

private:
    Ui::form_borrarproducto *ui;
};

#endif // FORM_BORRARPRODUCTO_H
