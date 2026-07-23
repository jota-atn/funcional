import java.util.Optional;

public class EmailServiceTest {

    private static final EmailService service = new EmailService();
    private static int total = 0;
    private static int passed = 0;

    public static void main(String[] args) {
        testGetEmailWithNullUser();
        testGetEmailWithNullEmail();
        testGetEmailSuccess();
        testGetEmailOptionalEmpty();
        testGetEmailOptionalNullEmail();
        testGetEmailOptionalSuccess();
        System.out.println(passed + "/" + total + " testes passaram");
    }

    static void assertEquals(Object expected, Object actual) {
        total++;
        if (expected == null ? actual == null : expected.equals(actual)) {
            passed++;
        } else {
            System.out.println("FALHOU: esperado <" + expected + ">, obtido <" + actual + ">");
        }
    }

    static void testGetEmailWithNullUser() {
        assertEquals("email não disponível", service.getEmail((User) null));
    }

    static void testGetEmailWithNullEmail() {
        assertEquals("email não disponível", service.getEmail(new User("Bob", null)));
    }

    static void testGetEmailSuccess() {
        assertEquals("alice@example.com", service.getEmail(new User("Alice", "Alice@Example.com")));
    }

    static void testGetEmailOptionalEmpty() {
        assertEquals("email não disponível", service.getEmail(Optional.empty()));
    }

    static void testGetEmailOptionalNullEmail() {
        assertEquals("email não disponível", service.getEmail(Optional.of(new User("Bob", null))));
    }

    static void testGetEmailOptionalSuccess() {
        assertEquals("alice@example.com",
                service.getEmail(Optional.of(new User("Alice", "Alice@Example.com"))));
    }
}
