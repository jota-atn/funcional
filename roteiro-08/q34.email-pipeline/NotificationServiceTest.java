import java.util.List;

public class NotificationServiceTest {

    private static final NotificationService service =
            new NotificationService(new UserRepository(), new EmailService());
    private static int total = 0;
    private static int passed = 0;

    public static void main(String[] args) {
        testMixedUsers();
        testEmptyList();
        testAllInvalid();
        System.out.println(passed + "/" + total + " testes passaram");
        System.exit(passed == total ? 0 : 1);
    }

    static void assertEquals(Object expected, Object actual) {
        total++;
        if (expected == null ? actual == null : expected.equals(actual)) {
            passed++;
        } else {
            System.out.println("FALHOU: esperado " + expected + ", obtido " + actual);
        }
    }

    static void testMixedUsers() {
        List<String> result = service.buildNotificationMessages(List.of(1, 2, 3, 99));
        assertEquals(
                List.of("Enviando email para alice@example.com",
                        "Enviando email para carol@test.com"),
                result);
    }

    static void testEmptyList() {
        List<String> result = service.buildNotificationMessages(List.of());
        assertEquals(List.of(), result);
    }

    static void testAllInvalid() {
        List<String> result = service.buildNotificationMessages(List.of(2, 99));
        assertEquals(List.of(), result);
    }
}
