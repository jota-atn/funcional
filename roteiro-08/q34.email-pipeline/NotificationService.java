import java.util.List;
import java.util.stream.Collectors;

public class NotificationService {

    private static final String EMAIL_INDISPONIVEL = "email não disponível";

    private final UserRepository repository;
    private final EmailService emailService;

    public NotificationService(UserRepository repository, EmailService emailService) {
        this.repository = repository;
        this.emailService = emailService;
    }

    public List<String> buildNotificationMessages(List<Integer> userIds) {
        return userIds.stream()
                .map(id -> emailService.getEmail(repository.findById(id)))
                .filter(email -> !email.equals(EMAIL_INDISPONIVEL))
                .map(email -> "Enviando email para " + email)
                .collect(Collectors.toList());
    }
}
