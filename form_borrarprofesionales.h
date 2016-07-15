#ifndef FORM_BORRARPROFESIONALES_H
#define FORM_BORRARPROFESIONALES_H

#include <QDialog>

namespace Ui {
class form_borrarprofesionales;
}

class form_borrarprofesionales : public QDialog
{
    Q_OBJECT

public:
    explicit form_borrarprofesionales(QWidget *parent = 0);
    ~form_borrarprofesionales();

private:
    Ui::form_borrarprofesionales *ui;
};

#endif // FORM_BORRARPROFESIONALES_H
