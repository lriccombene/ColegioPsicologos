#ifndef FORM_CONTRATOS_H
#define FORM_CONTRATOS_H

#include <QDialog>

namespace Ui {
class form_Contratos;
}

class form_Contratos : public QDialog
{
    Q_OBJECT

public:
    explicit form_Contratos(QWidget *parent = 0);
    ~form_Contratos();

private slots:
    void on_tabWidget_tabBarClicked(int index);

private:
    Ui::form_Contratos *ui;
};

#endif // FORM_CONTRATOS_H
