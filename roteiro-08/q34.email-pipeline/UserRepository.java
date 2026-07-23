import java.util.Map;
import java.util.Optional;

public class UserRepository {

    private final Map<Integer, User> users = Map.of(
            1, new User("Alice", "Alice@Example.com"),
            2, new User("Bob", null),
            3, new User("Carol", "Carol@Test.com"),
            4, new User("Dave", "Dave@Example.com"));

    public Optional<User> findById(int id) {
        return Optional.ofNullable(users.get(id));
    }
}
