#ifndef FORM_ACTUALIZARPROFESIONALES_H
#define FORM_ACTUALIZARPROFESIONALES_H

#include <QDialog>

namespace Ui {
class form_actualizarprofesionales;
}

class form_actualizarprofesionales : public QDialog
{
    Q_OBJECT

public:
    explicit form_actualizarprofesionales(QWidget *parent = 0);
    ~form_actualizarprofesionales();

private:
    Ui::form_actualizarprofesionales *ui;
};

#endif // FORM_ACTUALIZARPROFESIONALES_H
