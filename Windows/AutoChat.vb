Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        'Wait 2.5  Sec
        System.Threading.Thread.Sleep(2500)

        'Init Sender

        For Each line As String In TextBox1.Text.Split(vbLf)
            SendKeys.Send(line)
            SendKeys.Send("{Enter}")
            System.Threading.Thread.Sleep(2500)
        Next
End Sub
