// Main.qml
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Window 2.15

ApplicationWindow {
    id: mainWindow
    visible: true
    width: 400
    height: 300
    title: "File Sharer"

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20

        Label {
            text: "📁 File Sharing"
            font.pixelSize: 24
            horizontalAlignment: Text.AlignHCenter
            Layout.alignment: Qt.AlignHCenter
        }

        Button {
            text: "📤 Send a File"
            Layout.alignment: Qt.AlignHCenter
            onClicked: {
                // À connecter plus tard à Python
                console.log("Send a File clicked")
            }
        }

        Button {
            text: "📥 Start Server"
            Layout.alignment: Qt.AlignHCenter
            onClicked: {
                // À connecter plus tard à Python
                console.log("Start Server clicked")
            }
        }
    }
}
