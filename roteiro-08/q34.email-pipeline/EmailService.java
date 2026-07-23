import java.util.Optional;

public class EmailService {

    public String getEmail(User user) {
        if (user == null || user.getEmail() == null) {
            return "email não disponível";
        }
        return user.getEmail().toLowerCase();
    }

    public String getEmail(Optional<User> user) {
        return user
                .map(User::getEmail)
                .map(String::toLowerCase)
                .orElse("email não disponível");
    }
}
