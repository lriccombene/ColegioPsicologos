#ifndef FORM_SERVICIODECONTRATOS_H
#define FORM_SERVICIODECONTRATOS_H

#include <QDialog>

namespace Ui {
class form_serviciodecontratos;
}

class form_serviciodecontratos : public QDialog
{
    Q_OBJECT

public:
    explicit form_serviciodecontratos(QWidget *parent = 0);
    ~form_serviciodecontratos();

private:
    Ui::form_serviciodecontratos *ui;
};

#endif // FORM_SERVICIODECONTRATOS_H
